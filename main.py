from read_profiles import read_profiles
from rabby import rabby_login
from start_profiles import start_profile, init_driver


if __name__ == "__main__":
	profiles = read_profiles()
	for profile_id, profile_name in profiles.items():
		resp = start_profile(profile_id=profile_id, profile_name=profile_name)
		driver = init_driver(resp=resp)
		rabby_login(driver=driver, profile_name=profile_name)