import pandas as pd
from sklearn.utils import resample
def balanced_downsampling(df, label_col, second_col):
    """
    Perform balanced downsampling to ensure that each combination of label_col and second_col
    has the same number of samples, based on the smallest group size.

    Parameters:
    df (pd.DataFrame): Input dataframe.
    label_col (str): The primary column for balancing.
    second_col (str): The secondary column for balancing.

    Returns:
    pd.DataFrame: Dataframe with balanced downsampling.
    """
    # Find the smallest group size across all combinations of label_col and second_col
    min_count = df.groupby([label_col, second_col]).size().min()

    # Downsample each group to the smallest group size
    balanced_dfs = []
    for (label, second), group in df.groupby([label_col, second_col]):
        balanced_group = group.sample(min_count, random_state=42)
        balanced_dfs.append(balanced_group)

    return pd.concat(balanced_dfs)

def balanced_upsampling(df, label_col, second_col):
    """
    Perform balanced upsampling to ensure that each combination of label_col and second_col
    has the same number of samples, based on the largest group size.

    Parameters:
    df (pd.DataFrame): Input dataframe.
    label_col (str): The primary column for balancing.
    second_col (str): The secondary column for balancing.

    Returns:
    pd.DataFrame: Dataframe with balanced upsampling.
    """
    # Find the largest group size across all combinations of label_col and second_col
    max_count = df.groupby([label_col, second_col]).size().max()

    # Upsample each group to the largest group size
    upsampled_dfs = []
    for (label, second), group in df.groupby([label_col, second_col]):
        upsampled_group = resample(group, replace=True, n_samples=max_count, random_state=42)
        upsampled_dfs.append(upsampled_group)

    return pd.concat(upsampled_dfs)

def balanced_fixedcount(df, label_col, second_col, total_count):
    """
    Perform balanced sampling to ensure each combination of label_col and second_col has
    approximately total_count / number_of_combinations samples. Adjust the final count to
    match the total_count exactly.

    Parameters:
    df (pd.DataFrame): Input dataframe.
    label_col (str): The primary column for balancing.
    second_col (str): The secondary column for balancing.
    total_count (int): The total number of samples desired in the output dataframe.

    Returns:
    pd.DataFrame: Dataframe with balanced sampling.
    """
    # Number of unique combinations of label_col and second_col
    num_combinations = df.groupby([label_col, second_col]).ngroups

    # Determine the target number of samples per group
    target_per_group = total_count // num_combinations
    # Calculate the remainder to adjust the total sample count
    remainder = total_count % num_combinations

    # Collect the sampled data
    sampled_dfs = []
    for (label, second), group in df.groupby([label_col, second_col]):
        if len(group) > target_per_group:
            # Downsample to target_per_group
            sampled_group = group.sample(target_per_group, random_state=42)
        else:
            # Upsample to target_per_group
            sampled_group = resample(group, replace=True, n_samples=target_per_group, random_state=42)
        sampled_dfs.append(sampled_group)

    # If there is a remainder, adjust the final count
    if remainder > 0:
        # Identify groups to add one more sample
        additional_dfs = []
        for (label, second), group in df.groupby([label_col, second_col]):
            if len(group) >= target_per_group + 1:
                additional_group = group.sample(target_per_group + 1, random_state=42)
                additional_dfs.append(additional_group)
                remainder -= 1
                if remainder == 0:
                    break

        # Combine all sampled dataframes
        sampled_dfs.extend(additional_dfs)

    # Combine all sampled dataframes
    final_df = pd.concat(sampled_dfs)

    # Ensure the final count matches total_count
    final_df = final_df.sample(total_count, random_state=42)

    return final_df

# Example
data = {
    'label': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'A', 'B', 'C'],
    'second_col': ['X', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'Y', 'Z', 'Z', 'Z', 'Z']
}
df = pd.DataFrame(data)

upsampled_df = balanced_upsampling(df, label_col='label', second_col='second_col')
print(upsampled_df)
downsampled_df = balanced_downsampling(df, label_col='label', second_col='second_col')
print(downsampled_df)
fixed_df = balanced_fixedcount(df, 'label', 'second_col', 12)
print(fixed_df)
