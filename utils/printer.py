def user_printer(user):
      print(f"""\n     
       -----------------------------------------------------------------------------------------------
      |     ID: {user[0]}                                                                             

      |     First name: {user[1]}                                                                     
             
      |     Last name: {user[2]}                                                                      

      |     Create at: {user[6]}                                                                      

      |     Email: {user[3]}                                                                          

      |     Password: {user[4]}                                                                       

      |     Status: {user[5]}                                                                                       
                                                                                                                             
      | -----------------------------------------------------------------------------------------------
      
      """)
      return None


def region_printer(region):
      print(f"""\n   
       -----------------------------------------------------------------------------------------------
      |     ID: {region[0]}                                                                             

      |     Name: {region[1]}                                                                                                                                                         
                                                                                                                             
      | -----------------------------------------------------------------------------------------------
      """)
      return None


def city_printer(city):
      print(f"""\n         
       -----------------------------------------------------------------------------------------------
      |     ID: {city[0]}                                                                             

      |     Name: {city[1]}                                                                     
             
      |     Region ID: {city[2]}                                                                      
                                                                                                     
      | -----------------------------------------------------------------------------------------------
      """)
      return None


def season_printer(season):
      print(f"""\n
       -----------------------------------------------------------------------------------------------
      |     ID: {season[0]}                                                                             

      |     Start date: {season[1]}                                                                     
             
      |     End date: {season[2]}                                                                      

      |     Is active: {season[3]}                                                                      

      |     Status: {season[4]}                                                                          
                                                                                                        
      | -----------------------------------------------------------------------------------------------
      
      
""")
      return None


def appeal_printer(appeal):
      print(f"""\n
       -----------------------------------------------------------------------------------------------
      |     ID: {appeal[0]}                                                                             

      |     User ID: {appeal[1]}                                                                     
             
      |     City ID: {appeal[2]}                                                                      

      |     Information: {appeal[3]}                                                                      

      |     Is accepted: {appeal[4]}                                                                          

      |     Is active: {appeal[5]}                                                                       

      |     Total voice: {appeal[6]}                                                                        

      |     Status: {appeal[7]}                                                                         
                                                                                                                             
      | -----------------------------------------------------------------------------------------------
      
""")
      return None


def vote_printer(vote):
      print(f"""\nID: {vote[0]}     Start date: {vote[1]}   End date: {vote[2]}     Is active: {vote[3]}
            
                        Season ID: {vote[4]}     Is email: {[5]}  Status: {vote[6]}

       -----------------------------------------------------------------------------------------------
      |     ID: {vote[0]}                                                                             

      |     Start date: {vote[1]}                                                                     
             
      |     End date: {vote[2]}                                                                      

      |     Is active: {vote[3]}                                                                      

      |     Season ID: {vote[4]}                                                                          

      |     Is email: {vote[5]}                                                                       

      |     Status: {vote[6]}                                                                        
                                                                                                                             
      | -----------------------------------------------------------------------------------------------
      
""")
      return None


def voice_printer(voice):
      print(f"""\n
       -----------------------------------------------------------------------------------------------
      |     ID: {voice[0]}                                                                             

      |     Vote ID: {voice[1]}                                                                     
             
      |     Petition ID: {voice[2]}                                                                      

      |     User ID: {voice[3]}                                                                                                                                              
                                                                                                        
      | -----------------------------------------------------------------------------------------------
      
""")
      return None