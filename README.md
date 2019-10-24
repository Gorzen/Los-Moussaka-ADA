# Amazon food data analysis

## Abstract
Nowadays Amazon's popularity grows increasingly and becomes massive, it is ubiquitous in our era of cloud services and big data. Amazon has plenty of servers, buys big succesful companies such as Twitch, its CEO is the wealthiest man of our generation. But its underpinning is of course the website Amazon.

On Amazon you can buy almost any product nowadays, you can see users's ratings of any product, this of course changes the consumer's behavior. However, how much of an impact does it have on the consumer? Are there groups of consumers, groups that always buy the same stuff? On Amazon you can also see what related products people tend to look at after looking at the one you're looking at. Again, this most likely has an impact on sales, but is it possible to quantify it?

## Research questions
A list of research questions we would like to address during the project.

We can study different trends and their popularity at the product, the review or the reviewer level:
- What does the products' price distribution tell us?
- How are the prices and brands or sales rank related? 
- What can we infer about the reviewer from the helpfullness of their review?
- Is there a correlation between the quality of the review and the time at which the review has been posted? 
- How does the recommender system (`also bought` and `also viewed` fields) work? How much are the price, vendor or product type between recommended products correlated?

With PCA we can maybe study different questions using the review texts:
- Are there any trends in the comments
- Many people buy gifts on Amazon maybe we can extract some information about it:
	- To who do people buy gifts (husband, wife, children, ...)
	- Are some categories more gifted than others and to the same group of people 

## Dataset
Our dataset is _Amazon product data_, which contains around 150 millions of reviews from 1996 to 2014 along with their metadata. The metadata contains basic information like the product id, but also more complex information like a list of `also bought` and `also viewed` products that points to products related to the original one, on two different levels. This is extremely interesting to analyze, we can try to make assumptions on products' relations and verify them using this list. We can also try to find relations with these fields and analyze the results, as mentionned above. Concerning the actual reviews in the dataset, they contain all relevant information for a review: reviewer, time of the review, rating on the review, comment of the review. We will most likely use all of them to get insight on what the data tells us.

## A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

## Questions for TAs
- The Amazon dataset is named "Amazon reviews (Grocery and Gourmet Food category)" on the [provided data list](https://go.epfl.ch/ada19_datasets). However we think it'd be interesting to analyze the different categories altogether rather than only the "Grocery and Gourmet Food" one. Can we use the whole dataset? Will we still get TA support?
- Does the whole code need to be done for Milestone 2? With visualizations and analysis? Because it seems weird to have 1 month to do the **WHOLE** analysis and 1 month to write a 4 page report from that analysis. Can we still do further analysis after milestone 2? fancier visualization? and produce further results with the analysis? We don't really understand what exactly needs to be done for Milestone 2.
