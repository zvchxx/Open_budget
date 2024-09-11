def user_printer(user):
      print(f"""ID: {user[0]}, First name: {user[1]}, Last name: {user[2]}, 
                  Email: {user[3]}, Password: {user[4]}, Role ID: {user[5]},
                  Create at: {user[4]}""")
      return None


def region_printer(region):
      print(f"""ID: {region[0]}, Name: {region[1]}""")
      return None


def city_printer(city):
      print(f"""ID: {city[0]}, Name: {city[1]}, Region ID: {city[3]}""")
      return None