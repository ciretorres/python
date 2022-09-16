{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table border=\"1\" class=\"dataframe\">\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Longitude</th> <th>Latitude</th> <th>City Name</th> <th>Direction</th> <th>Survivors</th> <th>Percent Surviving</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td> <td>100.00%          </td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "        <tr>\n",
       "            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td> <td>96.55%           </td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "        <tr>\n",
       "            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td> <td>87.66%           </td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "        <tr>\n",
       "            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td> <td>68.97%           </td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "        <tr>\n",
       "            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td> <td>37.93%           </td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "        <tr>\n",
       "            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td> <td>16.55%           </td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "        <tr>\n",
       "            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td> <td>13.79%           </td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "        <tr>\n",
       "            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td> <td>8.28%            </td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "Longitude | Latitude | City Name   | Direction | Survivors | Percent Surviving\n",
       "32        | 54.8     | Smolensk    | Advance   | 145000    | 100.00%\n",
       "33.2      | 54.9     | Dorogobouge | Advance   | 140000    | 96.55%\n",
       "34.4      | 55.5     | Chjat       | Advance   | 127100    | 87.66%\n",
       "37.6      | 55.8     | Moscou      | Advance   | 100000    | 68.97%\n",
       "34.3      | 55.2     | Wixma       | Retreat   | 55000     | 37.93%\n",
       "32        | 54.6     | Smolensk    | Retreat   | 24000     | 16.55%\n",
       "30.4      | 54.4     | Orscha      | Retreat   | 20000     | 13.79%\n",
       "26.8      | 54.3     | Moiodexno   | Retreat   | 12000     | 8.28%"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from datascience import *\n",
    "\n",
    "## Minard's map\n",
    "minard = Table.read_table('http://inferentialthinking.com/notebooks/minard.csv')\n",
    "# print(minard)\n",
    "# print(minard.num_columns)\n",
    "# print(minard.num_rows)\n",
    "# print(minard.labels)\n",
    "minard = minard.relabeled('City', 'City Name')\n",
    "# print(minard.column('Survivors'))\n",
    "# print(minard.column(4))\n",
    "initial_size = minard.column('Survivors').item(0)\n",
    "# print(initial_size)\n",
    "percentage_surviving = minard.column('Survivors')/initial_size\n",
    "# print(percentage_surviving)\n",
    "with_percentages = minard.with_column(\n",
    "    'Percent Surviving', percentage_surviving\n",
    ")\n",
    "# print(with_percentages)\n",
    "with_percentages.set_format('Percent Surviving', PercentFormatter)\n",
    "\n",
    "#minard.select('Longitude', 'Latitude')\n",
    "#minard.select(0, 1)\n",
    "#minard.select('Survivors')\n",
    "#minard.drop('Longitude', 'Latitude', 'Direction')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
