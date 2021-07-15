from tradingAlgo import tradingAlgo

class dualMovingAverageCrossover(tradingAlgo):
    """
    Dual Moving Average Crossover trading algorithm 
    
    Handles only 1 price ticker. Utilizes a short term simple
    moving average and a long term simple moving average to 
    define bullish/bearish trend.
    """
    
    def __init__(self, short_lookback, long_lookback, time_of_bar='Close'):
        """
        Initialize an instance of class dualMovingAverageCrossover
        by specifying algorithm hyperparameters
        
        Parameters
        ----------
        short_lookback : int
            Number of bars to lookback for short term moving average
            
        long_lookback : int
            Number of bars to lookback for long term moving average
            
        time_of_bar : str from ['Open', 'High', 'Low', 'Close']
            Time of OHCL bar data to use for indicators
        """
        
        self._short_lookback = short_lookback
        self._long_lookback = long_lookback
        self._time_of_bar = time_of_bar
    
    def handle_data(self, data):
        """
        Called every time a bar of data is pushed from the backtesting
        or live trading API
        
        Parameters
        ----------
        data : pd.DataFrame
            OHCL price bars for the asset(s) of choice
        """
        
        px = data[self._time_of_bar].values
        if len(px) < self._long_lookback + 1:
            return 0
        signal = self._generate_signal(px)
        target = signal * 1.0
        return target
    
    def _generate_signal(self, px):
        """
        Generate trading signal given price data
        """
        
        sma = px[-self._short_lookback:].mean()
        lma = px[-self._long_lookback:].mean()
        if sma > lma:
            return 1
        else:
            return 0