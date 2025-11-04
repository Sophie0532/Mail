{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b19fad02",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np \n",
    "import os\n",
    "from datetime import datetime "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "83b7584c",
   "metadata": {},
   "outputs": [],
   "source": [
    "base_directory = r'Y:\\REGULATORIO MERCADOS\\DODD FRANK\\BAU DFA\\ESTRATEGICO 2025\\06. JUNIO\\Ficheros'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "753fc109",
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_file_to_df(filepath):\n",
    "    if filepath.endswith('xlsx'):\n",
    "\n",
    "        # If such a sheet is found, read it; otherwise, read the second sheet (index 1)\n",
    "        \n",
    "        df = pd.read_excel(filepath, dtype=str)\n",
    "        # Add the source filename to the DataFrame\n",
    "        filename = os.path.basename(filepath)\n",
    "        df['Source'] = filename\n",
    "        \n",
    "        return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dc25e27b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def process_files(directory, file_list):\n",
    "    dataframes = []\n",
    "    for filename in file_list:\n",
    "        print(f\"Processing file: {filename}\")\n",
    "        df = read_file_to_df(os.path.join(directory, filename))\n",
    "        dataframes.append(df)\n",
    "    aggregated_df = pd.concat(dataframes)\n",
    "    \n",
    "    return aggregated_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "893c5c82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Processing file: Submission_Management BAU - 02.06.xlsx\n",
      "Processing file: Submission_Management BAU - 03.06.xlsx\n",
      "Processing file: Submission_Management BAU - 04.06.xlsx\n",
      "Processing file: Submission_Management BAU - 05.06.xlsx\n",
      "Processing file: Submission_Management BAU - 06.06.xlsx\n",
      "Processing file: Submission_Management BAU - 09.06.xlsx\n",
      "Processing file: Submission_Management BAU - 10.06.xlsx\n",
      "Processing file: Submission_Management BAU - 11.06.xlsx\n",
      "Processing file: Submission_Management BAU - 12.06.xlsx\n",
      "Processing file: Submission_Management BAU - 13.06.xlsx\n",
      "Processing file: Submission_Management BAU - 16.06.xlsx\n",
      "Processing file: Submission_Management BAU - 17.06.xlsx\n",
      "Processing file: Submission_Management BAU - 18.06.xlsx\n",
      "Processing file: Submission_Management BAU - 19.06.xlsx\n",
      "Processing file: Submission_Management BAU - 20.06.xlsx\n",
      "Processing file: Submission_Management BAU - 23.06.xlsx\n",
      "Processing file: Submission_Management BAU - 24.06.xlsx\n",
      "Processing file: Submission_Management BAU - 25.06.xlsx\n",
      "Processing file: Submission_Management BAU - 26.06.xlsx\n",
      "Processing file: Submission_Management BAU - 27.06.xlsx\n",
      "Processing file: Submission_Management BAU - 30.06.xlsx\n"
     ]
    }
   ],
   "source": [
    "aggregated_file = process_files(base_directory,os.listdir(base_directory))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "64d217e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Source\n",
       "Submission_Management BAU - 04.06.xlsx    19201\n",
       "Submission_Management BAU - 06.06.xlsx    18114\n",
       "Submission_Management BAU - 16.06.xlsx    17900\n",
       "Submission_Management BAU - 11.06.xlsx    17882\n",
       "Submission_Management BAU - 05.06.xlsx    17516\n",
       "Submission_Management BAU - 26.06.xlsx    17167\n",
       "Submission_Management BAU - 12.06.xlsx    17038\n",
       "Submission_Management BAU - 10.06.xlsx    16977\n",
       "Submission_Management BAU - 13.06.xlsx    16697\n",
       "Submission_Management BAU - 03.06.xlsx    16575\n",
       "Submission_Management BAU - 02.06.xlsx    16458\n",
       "Submission_Management BAU - 27.06.xlsx    16445\n",
       "Submission_Management BAU - 17.06.xlsx    16040\n",
       "Submission_Management BAU - 09.06.xlsx    15981\n",
       "Submission_Management BAU - 30.06.xlsx    15948\n",
       "Submission_Management BAU - 25.06.xlsx    15719\n",
       "Submission_Management BAU - 18.06.xlsx    15684\n",
       "Submission_Management BAU - 23.06.xlsx    14767\n",
       "Submission_Management BAU - 20.06.xlsx    14749\n",
       "Submission_Management BAU - 24.06.xlsx    14737\n",
       "Submission_Management BAU - 19.06.xlsx    13635\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "aggregated_file['Source'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79ad9eb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "output_file_name = f'DFA_Junio_Acumulado.xlsx'\n",
    "aggregated_file.to_excel(os.path.join(base_directory,output_file_name),index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30675df5",
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
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
