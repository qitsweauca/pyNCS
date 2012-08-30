#-----------------------------------------------------------------------------
# Purpose:
#
# Author: Emre Neftci
#
# Copyright : University of Zurich, Giacomo Indiveri, Emre Neftci, Sadique Sheik, Fabio Stefanini
# Licence : GPLv2
#-----------------------------------------------------------------------------
from STas import events, channelEvents, RawOutput, channelAddressing, addrSpec
from STas import setDefaultMonChannelAddress, setDefaultSeqChannelAddress,\
                 getDefaultMonChannelAddress, getDefaultSeqChannelAddress
from STsl import SpikeList, STCreate
import pyST_globals
import numpy as np


def loadtxt(filename, comments, format='t'):
    data = np.loadtxt(filename, comments=comments)
    if format == 't':
        data = np.fliplr(data)
    ev = events(data, atype='l')
    id_list = np.unique(ev.get_ad())
    return SpikeList(ev.get_adtmev(), id_list)