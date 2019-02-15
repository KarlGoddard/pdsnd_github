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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("choose one of the following cities: chicago, new york city or washington \n").lower()
    while city not in CITY_DATA:
        print('Sorry that\'s not a valid input.')
        city = input("Please retry. Enter either: 'chicago', 'new york city' or 'washington' \n").lower()

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february','march','april','may','june']
    month = input("choose one of the following options: 'all' or one of the first six months of the year \n").lower()
    while month not in months:
        print('Sorry that\'s not a valid input.')
        month = input("Please retry. Enter either: 'all', 'january', 'february', 'march', 'april', 'may' or 'june' \n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input("choose one of the following options: 'all' or one of the days of the week \n").lower()
    while day not in days:
        print('Sorry that\'s not a valid input.')
        day = input("Please retry. Enter either: 'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' or 'sunday' \n").lower()

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months_dict = {1:'January', 2:'February', 3: 'March', 4:'April', 5:'May', 6: 'June'}
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month for travel is',months_dict[common_month],'\n')

    # display the most common day of week
    day_dict = {1:'Monday', 2:'Tuesday', 3: 'Wednesday', 4:'Thursday', 5:'Friday', 6: 'Saturday', 7:'Sunday'}
    df['day'] = df['Start Time'].dt.dayofweek
    common_day = df['day'].mode()[0]
    print('The most common day of the week to travel is on a',day_dict[common_day],'\n')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    if common_hour > 12:
        print('The most common hour for travel is',(common_hour-12),'pm \n')
    else:
        print('The most common hour for travel is',common_hour,'am \n')

    # ask user if they would like to look at the raw data
    show_lines = 0
    see_data = input('Do you want to see 5 lines of the raw data? Type "Yes" or "No" \n').lower()
    while True:
        if (see_data == 'yes'):
            print(df.iloc[show_lines], '\n')
            print(df.iloc[show_lines+1], '\n')
            print(df.iloc[show_lines+2], '\n')
            print(df.iloc[show_lines+3], '\n')
            print(df.iloc[show_lines+4], '\n')
            show_lines+=5
            see_data = input('Do you want to see 5 more lines of the raw data? Type "Yes" or "No" \n').lower()
            continue
        elif see_data == 'no':
            break
        else:
            print('Invalid input!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common station to start travel from is',common_start,'\n')

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly used station to end travel at is',common_end,'\n')

    # display most frequent combination of start station and end station trip
    start = df['Start Station']
    end = df['End Station']
    df['startend'] = start + ' to ' + end
    start_end = df['startend'].mode()[0]
    print('The most common combination of start to end station is',start_end,'\n')

    # ask user if they would like to look at the raw data
    # ask user if they would like to look at the raw data
    show_lines = 0
    see_data = input('Do you want to see 5 lines of the raw data? Type "Yes" or "No" \n').lower()
    while True:
        if (see_data == 'yes'):
            print(df.iloc[show_lines], '\n')
            print(df.iloc[show_lines+1], '\n')
            print(df.iloc[show_lines+2], '\n')
            print(df.iloc[show_lines+3], '\n')
            print(df.iloc[show_lines+4], '\n')
            show_lines+=5
            see_data = input('Do you want to see 5 more lines of the raw data? Type "Yes" or "No" \n').lower()
            continue
        elif see_data == 'no':
            break
        else:
            print('Invalid input!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tduration = df['Trip Duration'].sum()
    print('If all the journey times were added up, the total journey time for all users was',int(tduration/3600),'hours')
    print()

    # display mean travel time
    mduration = df['Trip Duration'].mean()
    print('The mean travel time for users was',mduration,'seconds')
    print()

    # ask user if they would like to look at the raw data
    show_lines = 0
    see_data = input('Do you want to see 5 lines of the raw data? Type "Yes" or "No" \n').lower()
    while True:
        if (see_data == 'yes'):
            print(df.iloc[show_lines], '\n')
            print(df.iloc[show_lines+1], '\n')
            print(df.iloc[show_lines+2], '\n')
            print(df.iloc[show_lines+3], '\n')
            print(df.iloc[show_lines+4], '\n')
            show_lines+=5
            see_data = input('Do you want to see 5 more lines of the raw data? Type "Yes" or "No" \n').lower()
            continue
        elif see_data == 'no':
            break
        else:
            print('Invalid input!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Here is a count of each User Type:')
    print()
    print(df.groupby(df['User Type'])['User Type'].count())
    print()

    # Display counts of gender
    if 'Gender' in df:
        print('Here is a count of each Gender:')
        print()
        print(df.groupby(df['Gender'])['Gender'].count())
        print()
    else:
        print('No gender information available in the bikeshare data for this city')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        firstyear = df['Birth Year'].min()
        lastyear = df['Birth Year'].max()
        mostyear = df['Birth Year'].mode()
        print('Here is some information about the recorded Birth Years:')
        print()
        print('The oldest user was born in',int(firstyear),'\n')
        print('The youngest user was born in',int(lastyear),'\n')
        print('The most common year that users were born was',int(mostyear),'\n')
        print()
    else:
        print('No birth year information available in the bikeshare data for this city')

    # ask user if they would like to look at the raw data
    show_lines = 0
    see_data = input('Do you want to see 5 lines of the raw data? Type "Yes" or "No" \n').lower()
    while True:
        if (see_data == 'yes'):
            print(df.iloc[show_lines], '\n')
            print(df.iloc[show_lines+1], '\n')
            print(df.iloc[show_lines+2], '\n')
            print(df.iloc[show_lines+3], '\n')
            print(df.iloc[show_lines+4], '\n')
            show_lines+=5
            see_data = input('Do you want to see 5 more lines of the raw data? Type "Yes" or "No" \n').lower()
            continue
        elif see_data == 'no':
            break
        else:
            print('Invalid input!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # retries the data set for the chosen city and iterates through 4 different functions that each focus on a separate aspect of the data.
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nDo you want to start again? Type "Yes" or "No" \n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
