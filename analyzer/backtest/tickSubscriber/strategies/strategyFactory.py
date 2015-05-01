'''
Created on Dec 26, 2011

@author: ppa
'''

from analyzer.backtest.tickSubscriber.strategies.periodStrategy import PeriodStrategy
from analyzer.backtest.tickSubscriber.strategies.smaStrategy import SMAStrategy
from analyzer.backtest.tickSubscriber.strategies.smaPortfolioStrategy import SMAPortfolioStrategy
from analyzer.backtest.tickSubscriber.strategies.zscorePortfolioStrategy import ZscorePortfolioStrategy
from analyzer.backtest.tickSubscriber.strategies.zscoreMomentumPortfolioStrategy import ZscoreMomentumPortfolioStrategy

from analyzer.lib.errors import Errors, UfException


class StrategyFactory(object):
    ''' Strategy factory '''
    STRATEGY_DICT = {'period': PeriodStrategy,
                     'sma': SMAStrategy,
                     'smaPortfolio': SMAPortfolioStrategy,
                     'zscorePortfolio': ZscorePortfolioStrategy,
                     'zscoreMomentumPortfolio': ZscoreMomentumPortfolioStrategy}

    @staticmethod
    def createStrategy(name, configDict):
        ''' create a metric '''
        if name not in StrategyFactory.STRATEGY_DICT:
            raise UfException(Errors.INVALID_STRATEGY_NAME,
                              "Strategy name is invalid %s" % name)
        return StrategyFactory.STRATEGY_DICT[name](configDict)

    @staticmethod
    def getAvailableTypes():
        ''' return all available types '''
        return StrategyFactory.STRATEGY_DICT.keys()