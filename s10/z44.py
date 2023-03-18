import random
import pandas as pd
data = pd.DataFrame(random.sample(['robot', 'human']*10, 20), columns={'whoAmI'})
data.head()
print(data)