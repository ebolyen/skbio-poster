# We need the "mapping" file, so we load it as a pandas dataframe
# Similar to the R dataframe
import pandas as pd
df = pd.read_csv("data/88-soils-map.txt", sep="\t", index_col=0)

from skbio import DistanceMatrix
from skbio.stats.ordination import PCoA

unifrac_dm = DistanceMatrix.read("data/88-soils.txt")
pcoa_results = PCoA(unifrac_dm).scores()
fig = pcoa_results.plot(df=df,
                        column="PH",
                        axis_labels=["PC 1", "PC 2", "PC 3"],
                        title="Samples colored by pH",
                        cmap="Reds",
                        s=35)
fig.savefig("../ordination_out.eps")
