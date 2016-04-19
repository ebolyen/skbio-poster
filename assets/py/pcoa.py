import pandas as pd
from skbio import DistanceMatrix
from skbio.stats.ordination import PCoA

unifrac_dm = DistanceMatrix.read("data/88-soils.txt")
pcoa_results = PCoA(unifrac_dm).scores()
df = pd.read_csv("data/88-soils-map.txt", "\t", index_col=0)
fig = pcoa_results.plot(df=df, column="PH", s=35, cmap="Reds",
                        axis_labels=["PC 1", "PC 2", "PC 3"],
                        title="Samples colored by pH")
fig.savefig("../ordination_out.eps")
