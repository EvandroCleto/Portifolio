import pandas as pd
import graphviz as graphviz

edu = [['B.Tech','CSE','2020','IIIT Jabalpur','8.1 CGPA'],['12th','Science','2016','Bhavan\'s KDKVM', '94.2%'],['10th','-','2012','Bhavan\'s KDKVM','10 CGPA']]

info = {'name':'Mehul Gupta', 'Brief':'Data Scientist with 2+ years of professional experience looking out to solve complex business problems using AI; Experienced in developing data-driven solutions for automating digitalization of health documents reducing manual efforts by 100% for lab reports & 50% for prescriptions; Love to learn new things. Right now : Streamlit !! ','photo':{'path':'abc.jpg','width':150}, 'Mobile':'8103795345','Email':'mehulgupta2016154@gmail.com','Medium':'https://medium.com/@mehulgupta_7991/about','City':'Nagda, Madhya Pradesh','Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/8422170/mehul-gupta"><img src="https://stackoverflow.com/users/flair/8422170.png?theme=clean" width="250" height="70"  alt="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>''','edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute','Score']),'skills':['Data Science','RDBMS','Cassandra','AWS Athena','Snowflake','Comet-ML','Python','Java','C++','Airflow','AWS S3','Tableau','Metabase','Thoughtspot','Streamlit'],'achievements':['Top AI writer @ Medium','1.4k+ reputation points on Stackoverflow','TCS humAIn Finalist,2019','25 Kaggle medals','Shikshan Bharati Kulapati K.M. Munshi Award in Mathematics,2014','Bharatiya Vidya Bhavan Shri C. Subramaniam Award for excellence in character, 2009 & 2012','Certificate of Merit(Proficiency in Co-curricular activities) for Declamation and Extempore'],'publication_url':'https://medium.com/data-science-in-your-pocket/tagged/beginner'}

paper_info = {'name':['Attended RPA of prescriptions','Algorithms for rapid digitalization of prescriptions'],'publication':['Elsevier','Elsevier'],'journal':['Smart Health','Visual Informatics'],'year':['2021','2021'],'role':['Co-Author','Author'],'Summary':['The paper revolves around the Prescription/Rx digitization pipeline deployed at Tata 1mg assisting the digitizer to fasten up the entire Rx validation process by ~5 seconds/Rx. As the platform recieves ~10k Rx, this solution saves nearly 14 hours of human labour daily !!','This is about a couple of algorithms namely, C-Cube (Capture-Cluster-Clean) & 3 Step Filtering helping in unassisted digitization of prescrptions (no human support required). Regarding latencies, we found that the C-Cube and the 3-Step Filtering algorithms were 588 and 231 times faster than the brute-force approach. In terms of accuracies, we found that the F-score of the C-cube algorithm was 90% higher than the F-score of the brute-force approach whereas the F-score for the 3-Step filtering algorithm was found to be 8600% higher.'],'file':['attented_rpa_of_prescriptions.pdf','algorithms_for_rapid_digitzation_of_prescriptions.pdf'],'images':{'0':[{'path':'images/rpa1.PNG','caption':'Digitization pipeline','width':600}],'1':[[{'path':'images/pr1.PNG','caption':'Capture seed words'},{'path':'images/pr2.PNG','caption':'cluster words using seed words'},{'path':'images/pr3.PNG','caption':'clean junk words'}],[{'path':'images/hw1.PNG','caption':'Filter 1'},{'path':'images/hw2.PNG','caption':'Filter 2'},{'path':'images/hw3.PNG','caption':'Filter 3'}]]}}

models = ('Fashion MNIST samples using GAN','Cycle GAN for Image Translation')
cycle_models = ('Winter to Summer','Summer to Winter')
cycle_model_url = {cycle_models[0]:['images/winter1.jpg','images/winter2.jpg','images/winter3.jpg'],cycle_models[1]:['images/summer1.jpg','images/summer2.jpg','images/summer3.jpg']}

rpa_metrics = pd.DataFrame([['Overall',66.4, 72.5],['printed rx',54.6, 64.6],['handwritten',67.3,73.3]], columns=['category','ds','non-ds'])
rapid_metrics = pd.DataFrame([['printed',91.6,70,79.4],['handwritten',21.1,34.7,26.2],['Brute-Force_Printed',29.9,82.7,41.8],['Brute-Force_Handwritten',0.2,62,0.3]],columns=['category','precision','recall','f1_score'])
rapid_metrics = rapid_metrics.set_index(['category'])

skill_col_size = 5
embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="evandro-cleto-51b49340" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://br.linkedin.com/in/evandro-cleto-51b49340?trk=profile-badge">Evandro Cleto</a></div>"""
		
		, 'medium':"""<div style="overflow-y: scroll; height:500px;"> <div id="retainable-rss-embed" 
data-rss="https://medium.com/feed/retainable,https://medium.com/feed/data-science-in-your-pocket"
data-maxcols="3" 
data-layout="grid"
data-poststyle="inline" 
data-readmore="Read the rest" 
data-buttonclass="btn btn-primary" 
data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""}



              