from bs4 import BeautifulSoup
import requests
import lxml
import replit
import colorama as cr
replit.clear()

cr.init(autoreset=True)



SubReddit = input("Which subreddit would you like to see popular posts for? r/").lower()



print("wait for the posts to load...")

url = ('https://www.reddit.com/r/' + SubReddit + '/top/?t=all')


headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}





response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.content, 'lxml')

Title = soup.title

print (url)
print('')
print('')
print (f"{cr.Fore.GREEN}there are no ads on this version of reddit!")
print ('')
print ('')
print ('')
print ('')



for item in soup.select('.Post'):
      if item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text() != '•' and "k" in (item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())and 'k' in (item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()):
            print(f"{cr.Fore.YELLOW}Post Title: " + f"{cr.Fore.WHITE}" + item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
            print('')
            print('Votes: ' + item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
            print('')
            print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())
            print('')
            
            try:
              print(f"{cr.Fore.YELLOW}Flair: " + f"{cr.Fore.WHITE}" + item.select('._2X6EB3ZhEeXCh1eIVA64XM')[0].get_text())
            except Exception as e:
              e = "No Flair"
              print(e)
            



            try:
              print (" "+ + item.select('._3Oa0THmZ3f5iZXAQ0hBJ0k ')[0])	
            except Exception as EEE:
              EEE = ""
              print(EEE)




            print(f"{cr.Fore.YELLOW}Original Post: " + f"{cr.Fore.WHITE}reddit.com" + item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])	

            print('')

            print('------------------------')



print("nothing Here? You might have entered an invalid subreddit or sort method!")


  
