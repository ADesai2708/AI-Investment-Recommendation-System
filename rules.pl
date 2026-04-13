% Risk profile rules
risk_profile(low, Age, Income) :-
    Age > 50 ;
    Income < 30000.

risk_profile(medium, Age, Income) :-
    Age =< 50,
    Age > 30,
    Income >= 30000.

risk_profile(high, Age, Income) :-
    Age =< 30,
    Income > 50000.

% Investment strategies
strategy(low, "Fixed Deposits, Bonds, Gold").

strategy(medium, "Balanced Mutual Funds, ETFs").

strategy(high, "Stocks, Crypto, High-growth Mutual Funds").

% Final recommendation
recommend(Age, Income, Strategy) :-
    risk_profile(Risk, Age, Income),
    strategy(Risk, Strategy).