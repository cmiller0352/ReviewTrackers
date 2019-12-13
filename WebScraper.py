from requests import get
from bs4 import BeautifulSoup

url = "https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183)"
def parseRow(row):
    core = {}
    title = row.find('p', attrs = {'class': 'reviewTitle'})
    text = row.find('p', attrs = {'class': 'reviewText'})
    name = row.find('p', attrs = {'class': 'consumerName'})
    name = name.text.strip().split()
    reviewDate = row.find('p', attrs = {'class': 'consumerReviewDate'})
    reviewDate = reviewDate.text.strip().split()
    numberOfStars = row.find('div', attrs = {'class': 'numRec'})
    upvotes = row.find('button', attrs = {'class': 'voteUp'})
    downvotes = row.find('button', attrs = {'class': 'voteDown'})
    core['title'] = title.text
    core['reviewText'] = text.text
    core['consumerName'] = name[0]
    core['state'] = name[-1]
    city = ' '.join(name[2:-1])
    city = city.replace(',', "")
    core['city'] = city
    core['reviewDate'] = ' '.join(reviewDate[-2:])
    core['numberOfStars'] = numberOfStars.text[1]
    core['upvotes'] = upvotes['data-voteupclick']
    core['downvotes'] = downvotes['data-votedownclick']
    return core


def get_reviews(url):
    r = get(url)
    data = []
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html5lib') 
        rows = soup.findAll('div', attrs = { 'class':'mainReviews' })
  
        for row in rows:
            rowData = parseRow(row)
            data.append(rowData)
    return data

if __name__ == '__main__':
    print(get_reviews(url))