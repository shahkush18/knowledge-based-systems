# knowledge-based-systems
1)  Research question: what is the group trying to learn or question to answer? Who is interested (audience)?

We have targeted a movie recommendation engine which would recommend movies to users, based on the ratings provided by other users.       
Recommendation systems are a very integral part of e-commerce websites as well as other service providers like online streaming (Netflix, Prime Video, etc) and many others.
Amazon has its own recommendation system which we often tend to use (“People who bought this also bought these items”). Netflix recommends movies based on preferred genres and ratings by users. 

2)  Domain and Data: Identify domain and source(s) of data
  
We have used a dataset released by grouplens from MovieLens website. The dataset contains 27,000,000 (27 million) anonymous ratings  of approximately 58,000 movies made by 280,000 MovieLens users.
Dataset Size is 1.13 GB. The dataset mainly has 3 files: movies.dat (it has movie id, title of the movie and genre.), ratings.dat (it contains user id, movie id, rating of the movie by user and timestamp) and personalized_rating.txt (it conains ratings by a particular user for whom we want to recommend movies). Dataset represents users and movies with integer ids. In all the files in dataset, data is separated by delimeter '::'. Ratings given by           users are from scale 1 to 5, 5 being the highest rating.

      
 3)  tentative plan for analysis on GCP

 i)  EDA and Preprocessing : Data has been already pre processed. We can directly work on it and implement the recommendation algorithm.
 ii)  Dashboard for User group, Dashboard for Data Engineers : We will plan to represent graphically the genres which are most recommended to a particular user. Also dashboards for the user to watch a movie if has likes the movie of same genre.
 iii)  GCP further processing - ML : We will use ALS(Alternative Least Square) algorithm which is Collaborative filtering algorithm built in Apache MLlib.
 iv)  Evaluation of results :  We will be evaluating our result by RMSE(Root Mean Square Error). The smaller the value is the accurate result will be. In ALS , we have different features as well , we will try to implement and tune the algorithm to get the least RMSE. 
 v)  Steps for production model : We will load our data in Predictive model which is based on ALS. Later on We will train our model with partial data and check RMSE . After training , we will be testing our model and prepare the model for Production data.
 vi)  Final Dashboard for User Group: Finally, users will view the what movies have been most recommended. This will be based on the movie and user matrix that will help to recommend movies to users based on the ratings given by users.
