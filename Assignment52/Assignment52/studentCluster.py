import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    # 1. Load dataset
    df = pd.read_csv('student_performance_ml.csv')

    # 2. Select numeric features only
    numeric_df = df.select_dtypes(include=['int64', 'float64'])

    # 3. Handle missing values
    numeric_df = numeric_df.fillna(numeric_df.mean())

    # 4. Scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)

    # 5. Apply KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(scaled_data)

    # 6. Interpret clusters based on performance
    cluster_means = df.groupby('cluster')[numeric_df.columns].mean()

    cluster_ranking = cluster_means.mean(axis=1).sort_values(ascending=False)

    cluster_mapping = {
        cluster_ranking.index[0]: 0,  # Top performers
        cluster_ranking.index[1]: 1,  # Average
        cluster_ranking.index[2]: 2   # Struggling
    }

    df['performance_group'] = df['cluster'].map(cluster_mapping)

    # Show results
    print(df[['cluster', 'performance_group']].head())

    # 7. distribution
    print("\nCluster Distribution:")
    print(df['performance_group'].value_counts())

if __name__=="__main__":
    main()