# knowledge-based-systems
1)  Research question: what is the group trying to learn or question to answer? Who is interested (audience)?

We have targeted a movie recommendation engine which would recommend movies to users, based on the ratings provided by other users.       
Recommendation systems are a very integral part of e-commerce websites as well as other service providers like online streaming (Netflix, Prime Video, etc) and many others.
Amazon has its own recommendation system which we often tend to use (“People who bought this also bought these items”). Netflix recommends movies based on preferred genres and ratings by users. 

2)  Domain and Data: Identify domain and source(s) of data
  
We have used a dataset released by grouplens from MovieLens website. The dataset contains 27,000,000 (27 million) anonymous ratings  of approximately 58,000 movies made by 280,000 MovieLens users.
Dataset Size is 1.13 GB. The dataset mainly has 3 files: movies.dat (it has movie id, title of the movie and genre.), ratings.dat (it contains user id, movie id, rating of the movie by user and timestamp) and personalized_rating.txt (it conains ratings by a particular user for whom we want to recommend movies). Dataset represents users and movies with integer ids. In all the files in dataset, data is separated by delimeter '::'. Ratings given by           users are from scale 1 to 5, 5 being the highest rating.

      
      c)  tentative plan for analysis on GCP

           1)  EDA and Preprocessing : 
           
           2)  Dashboard for User group, Dashboard for Data Engineers :

           3)  GCP further processing - ML

           4)  Evaluation of results

           5)  Steps for production model

           6)  Final Dashboard for User Group


