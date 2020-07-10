import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = {'january', 'february', 'march' , 'april', 'may', 'june', 'all'}
days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
month_match = {'january': 1,'february': 2,'march': 3,'april': 4,'may': 5,'june': 6}
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please select chigago, new york city or washington  ').lower()
        if city in CITY_DATA:
            print('You have selected', city)
            break
        else:
            print('You did not select a valid city please select from chigago, new york city or washington')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please select a month from january through June or all  ').lower()
        if month in months:
            print ('You have selected', month)
            break
        else:
                print('You did not select a valid month please select all or a month from january through June')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please select a day of the week  ').lower()
        if day in days:
            print('You have selected', day)
            break
        else:
                print('You did not select a valid day please select a day of the week. Example monday')

    #This will display a long line
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday

    if month != 'all':
        month_name=['january','february','march','april','may','june']
        month= month_name.index(month)+ 1
        df=df[df['month'] == month]

    if day != 'all':
        day_name=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day=day_name.index(day) + 1
        df=df[df['weekday']== day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    Common_Month = df['month'].mode()[0]-1
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_popular_month = months[Common_Month - 1]
    print('Most common month', most_popular_month)

    # TO DO: display the most common day of week
    common_day = df['weekday'].mode()[0]
    days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
    most_popular_day = days[common_day - 1]
    print('Most common day of week', most_popular_day)
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour= df['hour'].mode()[0]
    print('Most common hour of the day', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station =df['Start Station'].mode().values[0]
    print('Most commonly used Start Station', start_station)


    # TO DO: display most commonly used end station
    end_station =df['End Station'].mode().values[0]
    print('Most Commonly used End Station',end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station']+ 'to' + df['End Station']
    frequent_combination = df['start_end'].mode().values[0]
    print('most Frequent start and stop station', frequent_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('Total Travel Time',trip_duration)


    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('Mean Travel Time', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_usertype = df['User Type'].value_counts()
    print('Count of User Types', count_usertype)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_gender = df['Gender'].value_counts()
        print('Count of Gender', count_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest= df['Birth Year'].min()
        most_recent=df['Birth Year'].max()
        most_common=df['Birth Year'].mode()[0]
        print('Earliest Bithday', earliest)
        print('Most Recent', most_recent)
        print('Most Common', most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i=0
        raw = input('Would you like to see 5 lines of raw data? yes or no?').lower
        while True:
            if raw=='no':
                break
            print(df[i:i+5])
            raw= input(' want to see 5 more lines of data yes or no?').lower()
            i += 5



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
