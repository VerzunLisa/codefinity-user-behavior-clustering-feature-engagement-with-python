import pandas as pd
import matplotlib.pyplot as plt

def analyze_retention_drivers(df, feature_cols, retention_col):
    correlations = {}
    for feature in feature_cols:
        corr = df[retention_col].corr(df[feature])
        correlations[feature] = corr
    sorted_features = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)
    top_features = sorted_features[:3]
    top_feature_names = [f[0] for f in top_features]
    top_corrs = [f[1] for f in top_features]
    fig, ax = plt.subplots()
    bars = ax.bar(top_feature_names, top_corrs, color='skyblue')
    ax.set_title("Correlation with Retention")
    ax.set_ylabel("Top 3 Retention-Driving Features")
    plt.show()
    recommendations = []
    for feature, corr in top_features:
        if corr > 0.5:
            rec = f"Highlight '{feature}' in onboarding and add in-app prompts."
        elif corr > 0.3:
            rec = f"Add contextual tips for '{feature}' and monitor engagement."
        else:
            rec = f"Consider targeted campaigns for '{feature}'."
        recommendations.append((feature, corr, rec))
    return recommendations


# Sample DataFrame
data = {
    'feature_A': [5, 2, 3, 7, 4, 6, 1],
    'feature_B': [1, 4, 2, 2, 3, 3, 5],
    'feature_C': [0, 1, 0, 1, 1, 0, 1],
    'feature_D': [8, 2, 5, 7, 6, 4, 3],
    'retained':   [1, 0, 0, 1, 1, 1, 0]
}
df = pd.DataFrame(data)
feature_cols = ['feature_A', 'feature_B', 'feature_C', 'feature_D']
retention_col = 'retained'

recommendations = analyze_retention_drivers(df, feature_cols, retention_col)
summary = pd.DataFrame(recommendations, columns=["Feature", "Correlation Score", "Recommended Intervention"])
print(summary)
