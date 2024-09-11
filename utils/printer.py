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


def appeal_printer(appeal):
      print(f"""ID: {appeal[0]}, Start date: {appeal[1]}, 
                  End date: {appeal[2]}, Is active: {appeal[3]}, Season ID {[4]},
                  Total appeals{[5]}, Status: {appeal[6]}""")
      return None


def petition_printer(petition):
      print(f"""ID: {petition[0]}, Title: {petition[1]}, 
                  Content: {petition[2]}, Money: {petition[3]}, 
                  City ID: {petition[4]}, Is winner: {petition[5]}, Is accepted: {petition[6]},
                  Appeal ID: {petition[7]}, Category ID: {petition[8]}, Total voices: {petition[9]},
                  Status: {petition[100]}, User ID: {petition[11]}""")
      return None