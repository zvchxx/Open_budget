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


def category_printer(category):
      print(f"""ID: {category[0]}, Name: {category[1]}, Status: {category[3]}""")
      return None


def season_printer(season):
      print(f"""ID: {season[0]}, Start date: {season[1]}, 
                  End date: {season[2]}, Is active: {season[3]}, Status: {season[4]}""")
      return None