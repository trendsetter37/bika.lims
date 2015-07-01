from bika.lims.interfaces import ISample
from plone.indexer import indexer
from bika.lims.indexers.analysisrequest import Analysts as ARAnalysts

@indexer(ISample)
def Analysts(instance):
    analysts = []
    for ar in instance.getAnalysisRequests():
        analysts.extend(ARAnalysts(ar))
    return analysts

@indexer(ISample)
def Sampler(instance):
    return instance.getSampler()

@indexer(ISample)
def Preserver(instance):
    return instance.getPreserver()

@indexer(ISample)
def ClientSampleID(instance):
    return instance.getClientSampleID()