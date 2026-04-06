import matplotlib.pyplot as plt



def show_graph(df):
    df["age"].hist(bins=20)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()



# df["income"].hist(bins=30)
# plt.title("Income Distribution")
# plt.xlabel("Income")
# plt.ylabel("Count")
# plt.show()

def scatter_income_spend(df):
    plt.scatter(df["income"], df["spend_score"], alpha=0.3)
    plt.title("Income vs Spend Score")
    plt.xlabel("Income")
    plt.ylabel("Spend Score")
    plt.show()
