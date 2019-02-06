#================How to Use==================#
"""
1 main Class
Indeed will do the necessary updates for indeed.
Import into shell and create an instance of Indeed to run.
This code definitely needs refactoring.

"""
class Indeed():

    def __init__(self):
        self.jobtitles,self.links,self.company,self.unique_ids= self.indeed_pull()
        self.indeed_update_database(self.jobtitles,self.links,self.company,self.unique_ids)

    def indeed_pull(self):
        from urllib.request import urlopen as uReq
        from bs4 import BeautifulSoup as soup
        base_url = "https://www.indeed.com/jobs?q=Python+developer&l=San+Antonio%2C+TX"
        #helper function
        def scrape_soup_2(all_job_boxes,jobtitles,links,company_names,unique_ids):
            #Run this only when you are feeding empty strings.
            link_base = "https://www.indeed.com"
            for i,job in enumerate(all_job_boxes):
                anchors = job.select('a.jobtitle')
                #this is the case without h2 tags
                if len(anchors)==1:
                    current_title= anchors[0].get('title').strip()
                    current_link = link_base+anchors[0].get('href')
                #this is the case with h2 tags. h2 > a.title
                else:
                    h2s= job.select("h2.jobtitle")
                    link = h2s[0].select("a.turnstileLink")
                    if len(h2s) == 1:
                        current_title = h2s[0].a.get('title').strip()
                        current_link = link_base+link[0].get('href')
                #========Company Names================#
                company_span = job.select('span.company')
                company_anchor = company_span[0].select('a')
                    #==========1.No company links ==========#
                if len(company_anchor) == 0:
                    current_company = company_span[0].text.strip()
                    #==========2.company links ==========#
                else:
                    current_company = company_anchor[0].text.strip()
                unique_id = current_company+current_title
                #Only addition to scrape soup 1 since we are not starting with empty unique ids. 
                #realistically i can JUST use this.
                if unique_id not in unique_ids:
                    jobtitles.append(current_title)
                    links.append(current_link)
                    company_names.append(current_company)
                    unique_ids.append(unique_id)
            return jobtitles,links,company_names,unique_ids

        starts_with = 0
        jobtitles,links,company_names,unique_ids = [],[],[],[]
        while starts_with < 100:
            #should do 10,20,30,40
            if starts_with == 0:
                url = base_url
            else:
                url = base_url + "&start="+str(starts_with)
            print(len(jobtitles))
            print("crawling: \n")
            print(url)
            print(len(jobtitles))
            uClient = uReq(url)
            page_html= uClient.read()
            uClient.close()
            #parse soup
            page_soup = soup(page_html, 'html.parser')
            all_job_boxes = page_soup.findAll("div",{"class":"jobsearch-SerpJobCard"})
            jobtitles,links,company_names,unique_ids = scrape_soup_2(
                all_job_boxes,jobtitles,links,company_names,unique_ids
                )
            starts_with += 10
        
        return jobtitles,links,company_names,unique_ids

    def indeed_update_database(self,jobtitles,links,company_names,unique_ids):
        from jobs.models import Job 
        from datetime import date
        current_jobs = Job.objects.all()
        current_links =[]
        for job in current_jobs:
            current_links.append(job.job_link)
        for i in range(len(jobtitles)):
            if links[i] not in current_links:
                Job.objects.create(
                    job_title= jobtitles[i],
                    job_company = company_names[i],
                    job_link = links[i],
                    job_last_action=date.today(),
                )

