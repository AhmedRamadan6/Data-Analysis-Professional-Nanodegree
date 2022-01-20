import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("Please specify a city from (chicago, new york city, washington)\n").lower()
      if city in CITY_DATA:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("Please specify a month from (January, February, March, April, May, June) or type all\n").lower()
      mths = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
      if month in mths:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("Please specify a day from  (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) or type all\n").lower()
      dys = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
      if day in dys:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        mths = ['january', 'february', 'march', 'april', 'may', 'june']
        month = mths.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("would you like to see some raw data type yes or no\n").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("would you like to see more raw data type yes or no\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', common_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    Common_Hour = df['hour'].mode()[0]
    print('The most common start hour:', Common_Hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Common = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', Start_Common)


    # TO DO: display most commonly used end station

    End_Common = df['End Station'].value_counts().idxmax()
    print('\nMost commonly used end station:', End_Common)


    # TO DO: display most frequent combination of start station and end station trip

    combination = (df['Start Station'] + " and " + df['End Station']).mode()[0]

    print('\nMost frequent combination of start station and end station trip:', combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', round(Total_Travel_Time/86400), " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', round(Mean_Travel_Time/60), " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n',user_types)

    # TO DO: Display counts of gender

    if 'Gender' in df:
          print('\nCount of gender types:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
      earliest = df['Birth Year'].min()
      print('\nEarliest year:',int(earliest))

      Most_Recent = df['Birth Year'].max()
      print('\nMost recent year:',int(Most_Recent))
   

      Most_Common = df['Birth Year'].value_counts().idxmax()
      print('\nMost common year:',int(Most_Common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while (1):
            if restart.lower() != 'yes' and restart.lower() != 'no':
                restart = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            else:
                break
        if restart.lower() == 'no':
            break


if __name__ == "__main__":
	main()