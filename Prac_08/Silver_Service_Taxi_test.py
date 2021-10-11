from Prac_08.Silver_Service_Taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Fancy Taxi 1", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
