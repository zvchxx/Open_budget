def user_printer(user):
      print(f"""\nID: {user[0]},      First name: {user[1]},        Last name: {user[2]}, 
                Email: {user[3]},   Password: {user[4]},          Status: {user[5]},
                                    Create at: {user[6]}""")
      return None


def region_printer(region):
      print(f"""\nID: {region[0]},     Name: {region[1]}""")
      return None


def city_printer(city):
      print(f"""\nID: {city[0]},       Name: {city[1]}, 
            
                        Region ID: {city[2]}""")
      return None


def season_printer(season):
      print(f"""\nID: {season[0]},    Start date: {season[1]},      End date: {season[2]}, 
            
                        Is active: {season[3]},      Status: {season[4]}""")
      return None


def appeal_printer(appeal):
      print(f"""\nID: {appeal[0]}    User ID: {appeal[1]}   City ID: {appeal[2]}    Information: {appeal[3]}
            
                   Is accepted: {appeal[4]}      Is active:{appeal[5]}   Total voice: {appeal[6]}     

                              IS winner: {appeal[7]}   Status: {appeal[8]}""")
      return None


def vote_printer(vote):
      print(f"""\nID: {vote[0]}     Start date: {vote[1]}   End date: {vote[2]}     Is active: {vote[3]}
            
                        Season ID: {vote[4]}     Is email: {[5]}  Status: {vote[6]}""")
      return None


def voice_printer(voice):
      print(f"""\nID: {voice[0]}        Vote ID: {voice[1]}
            
            Petition ID: {voice[2]}        User ID: {voice[3]}""")
      return None