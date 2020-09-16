from napalm import get_network_driver
import os
import sys


print(get_network_driver('ios'))


def main(config_file):
    global device
    '''Import a configuration file here'''
    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = "Missing or invalid config file {0}".format(config_file)
        raise ValueError(msg)

    driver = get_network_driver('iosxr')

    device = driver(hostname="127.0.0.1",
        username="vagrant",
        password="vagrant",
        optional_args={"port": 12443},
    )

    device.open()
    device.load_replace_candidate(filename='')
    print(device.compare_config())

    try:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == "y":
        print("Committing ...")
        device.commit_config()
    else:
        print("Discarding ...")
        device.discard_config()

        device.close()
        print("Done.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please supply the full path to the file')
        sys.exit(1)
    config_file = sys.argv[1]
    main(config_file)


