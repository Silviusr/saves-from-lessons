import pandas as pd
import numpy as np
import random
from collections import deque

class CustomEnv:
    def __init__(self, df, initial_balance = 1000, lookback_windowsize = 50):
        self.df = df.dropna().reset_index()
        self.df_total_steps = len(self.df)-1
        self.initial_balance = initial_balance
        self.lookback_windowsize = lookback_windowsize
        self.action_space = np.array([1,2,3])
        self.order_history = deque(maxlen=self.lookback_windowsize)
        self.market_history = deque(maxlen=self.lookback_windowsize)
        self.state_size = (self.lookback_windowsize, 10)

    def reset(self, env_step_size = 0):
        self.balance = self.initial_balance
        self.net_worth = self.initial_balance
        self.prev_net_worth = self.initial_balance
        self.crypto_held = 0
        self.crypto_sold = 0
        self.crypto_bought = 0
        if env_step_size > 0:
            self.start_step = random.randint(self.lookback_windowsize, self.df_total_steps - env_step_size)
            self.end_step = self.start_step + env_step_size
        else:
            self.start_step = self.lookback_windowsize
            self.end_step = self.df_total_steps
        self.current_step = self.start_step
        for i in reversed(range(self.lookback_windowsize)):
            current_step = self.current_step - i
            self.order_history.append([self.balance, self.net_worth, self.crypto_bought, self.crypto_sold, self.crypto_held])
            self.market_history.append([self.df.loc[current_step, 'Open'],
                                        self.df.loc[current_step, 'High'],
                                        self.df.loc[current_step, 'Low'],
                                        self.df.loc[current_step, 'Close'],
                                        self.df.loc[current_step, 'Volume']
                                        ])
        state = np.concatenate((self.market_history, self.order_history), axis=1)
        return state
    def step(self, action):
        self.crypto_bought = 0
        self.crypto_sold = 0
        self.current_step += 1
        current_price =  random.uniform(self.df.loc[self.current_step, 'Open'],
                                        self.df.loc[self.current_step,'Close'])
        if action == 0:
            pass
        elif action == 1 and self.balance > 0:
            self.crypto_bought = self.balance / current_price
            self.balance -= self.crypto_bought*current_price
            self.crypto_held += self.crypto_bought
        elif action == 2 and self.crypto_held > 0:
            self.crypto_sold = self.crypto_held
            self.balance = self.crypto_sold * current_price
            self.crypto_held -= self.crypto_sold
        self.prev_net_worth = self.net_worth
        self.net_worth = self.balance + self.crypto_held * current_price
        self.order_history.append([self.balance, self.net_worth, self.crypto_bought, self.crypto_sold, self.crypto_held])
        reward = self.net_worth - self.prev_net_worth
        if self.net_worth <= self.initial_balance/2:
            done = True
        else:
            done = False
        obs = self.next_observation()
        return obs, reward, done
    def next_observation(self):
        self.market_history.append([self.df.loc[self.current_step, 'Open'],
                                        self.df.loc[self.current_step, 'High'],
                                        self.df.loc[self.current_step, 'Low'],
                                        self.df.loc[self.current_step, 'Close'],
                                        self.df.loc[self.current_step, 'Volume']
                                        ])
        obs = np.concatenate((self.market_history, self.order_history), axis=1)
        return obs
    def render(self):
        print(f'Step: {self.current_step}, Net Worth: {self.net_worth}')
    
