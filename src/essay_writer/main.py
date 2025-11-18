import warnings
warnings.filterwarnings("ignore")

from essay_writer.ewriter import EWriter, writer_gui

multi_agent = EWriter()
app = writer_gui(multi_agent.graph, True)
app.launch()
