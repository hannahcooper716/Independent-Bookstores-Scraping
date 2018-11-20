from bs4 import BeautifulSoup
import requests

# html = requests.get('https://www.newpages.com/independent-bookstores/arizona-bookstores').text
# soup = BeautifulSoup(html, 'html.parser')
# searching_div = soup.find('div', class_ = 'tm-main uk-width-medium-3-5 uk-push-1-5')
class Bookstores:
    def __init__(self, name = 'No Name', link=None, phone = "phone"):
        self.name = name
        self.link = link

        self.phone = phone

    def __str__(self):
        return '{}: {}, {}'.format(self.name, self.link, self.phone)

def info(state):
    baseurl = 'https://www.newpages.com/independent-bookstores/{}-bookstores'.format(state)
    html = requests.get(baseurl).text
    soup = BeautifulSoup(html, 'html.parser')
    searching_div = soup.find('div', class_ = 'tm-main uk-width-medium-3-5 uk-push-1-5')
    #print(searching_div)
    information = searching_div.find_all('div', class_ = 'catItemExtraFields')
    #print(information)
    list_of_info = []
    for x in information:
        ty = x.find_all('li', class_ = 'odd typeSelect group13 ibsTYpe')
        #print(ty)
        for t in ty:
            type_ = t.find('span', class_ = 'catItemExtraFieldsValue').text
            #print(type_)
            if type_ != "Used books" and type_ != "Children's":
                # print('here')
                name = x.find('a').text
                #print(name)
                link = x.find('a')['href']
                #print(link)
                # locationname = x.find('span', class_ = 'catItemExtraFieldsValue').text
                phonenumber = x.find_all('li', class_ = 'even typeTextfield group13 ibsPhone')
                for y in phonenumber:
                    phone = y.find('span', class_ = 'catItemExtraFieldsValue').text
                    all_info = Bookstores(name = name, link = link, phone = phone)
                        #print(number)
                    list_of_info.append(all_info)

    return list_of_info
                #print(type_)
                #print('---------------')


        #locationname = x.find('span', class_ = 'catItemExtraFieldsValue').text
        #print(locationname)
                    # name = x.find('a').text
                    # print(name)
                    # link = x.find('a')['href']
                    # print(link)
                    # # locationname = x.find('span', class_ = 'catItemExtraFieldsValue').text
                    # phone = x.find_all('li', class_ = 'even typeTextfield group13 ibsPhone')
                    # for y in phone:
                    #     number = y.find('span', class_ = 'catItemExtraFieldsValue').text
                    #     print(number)
                    # print(type_)
                # if type_ == "Used books":
                #     continue
        # ty = x.find_all('li', class_ = 'odd typeSelect group13 ibsTYpe')
        # for t in ty:
        #     type_ = t.find('span', class_ = 'catItemExtraFieldsValue').text
        #     if type_ == 'Used books':
        #         continue
            # print(type_)
                # print('----------------')

# info(state)

if __name__ == "__main__":
    resp = input('Enter command (or “help” for options): ')
    while resp != "exit":
        number = 0
        #if "list" in resp:
        abbreviations = {
            'alabama',
            'alaska',
            'arizona',
            'arkansas',
            'california',
            'colorado',
            'connecticut',
            'delaware',
            'florida',
            'georgia',
            'hawaii',
            'idaho',
            'illinois',
            'indiana',
            'iowa',
            'kansas',
            'kentucky',
            'louisiana',
            'maine',
            'maryland',
            'massachusetts',
            'michigan',
            'minnesota',
            'mississippi',
            'missouri',
            'montana',
            'nebraska',
            'nevada',
            'new-hampshire',
            'new-jersey',
            'new-mexico',
            'new-york',
            'north-carolina',
            'north-dakota',
            'ohio',
            'oklahoma',
            'oregon',
            'pennsylvania',
            'rhode-island',
            'south-carolina',
            'south-dakota',
            'tennessee',
            'texas',
            'utah',
            'vermont',
            'virginia',
            'washington',
            'west-virginia',
            'wisconsin',
            'wyoming'}
        list_ = {}
        if resp in abbreviations:
            s = info(resp)
        for x in s:
            number = number + 1
            list_[x] = number
            print(str(number) + " " + x.__str__())
        resp = input('Enter command (or “help” for options): ')
        if 'exit' == resp:
            print('Bye!')
            break

            # list_ = {}
            # split = resp.split()
            # for x in abbreviations:
            #     if abbreviations[x] == split[0].lower():
            #         state = x
            #     print('Bookstores in ' + state)
            #     places__ = info(split[1])
            #     for x in places__:
            #         number = number + 1
            #         list_[x] = number
            #         print(str(number) + " " + x.__str__())

    # for x in information:
    #location = searching_div.find_all('li', class_ = 'even typeTextfield group13 ibsCitYTitle')
    #link = searching_div.find_all('li', class_ = 'odd typeLink group13 ibsTitleLink')
    #print(link)
    #print(location)
    # for x in location:
    # for x in searching_div:
    #     locationname = x.find_all('span', class_ = 'catItemExtraFieldsValue').text
    #     print(locationname)
    # for x in link:
    #     link = x.find('a')['href']
    #     name = x.find('span', class_ = "catItemExtraFieldsValue").text
        # print(name)
        # print(link)










# searching_div = soup.find('div', class_ = 'catItemExtraFields')
# for x in searching_div:
#     number = x.find('span', class_ = 'catItemExtraFieldsValue')

# print(searching_div)

# print(soup.prettify())

#
# baseurl = 'https://www.newpages.com/independent-bookstores/{}-bookstores'.format(state_abbr)
#   html = make_request_using_cache(baseurl)
