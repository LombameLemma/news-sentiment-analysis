from scipy.stats import pearsonr

def calculate_correlation(sentiment, returns):

    corr, p_value = pearsonr(sentiment, returns)

    return {
        "correlation": corr,
        "p_value": p_value
    }