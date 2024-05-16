**Video Game Success Prediction Data Specification**

## Overview
This document outlines the data specifications for the video game dataset used in the development of a statistical model to predict the success of video games. The dataset comprises various attributes such as game ID, name, description, genre(s), platform(s), reviews, development company, review scores, release date, and review date.

## Summary of challenges and observations since collecting the data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. 
Since collecting data, we've encountered challenges in obtaining metrics such as budget, selling price, most searched, franchise information, and game specifications like number of players. Although one of our sources had information about prices, the data is limited to access through an API.  These gaps limit our ability to conduct comprehensive analysis, particularly in understanding budget allocations, popularity trends, and franchise performance. Our next steps involve optimizing our existing dataset by enriching it with additional sources where possible and leveraging advanced analytics techniques to derive insights despite the limitations. We'll focus on analyzing the available data to identify trends in genre preferences, platform popularity, and review scores to inform decision-making processes in the gaming industry. Besides some attributes and records that were difficult or limited to collect we encountered issues with the size of the extracted data for the IGDB source where entries surpassed 300,000. 

## Data Format
The data is stored in JSON format, with each record representing a single video game. Below is a breakdown of the attributes (some found in specific data bases) and their specifications:

1. **Game ID**
  - Data Type: Integer
  - Unique Values: Yes
  - Used for Duplicate Detection: Yes, by cross-referencing with other attributes.
Using as PRIMARY KEY in our data bases
  - Required: No, ID varies from one API to another
  - Used in Analysis: No
  - Sensitive Information: No

2. **Name**
  - Data Type: String
  - Range of Values: Alphanumeric
  - Used in Analysis: Used for identification, labeling
  - Used for Duplicate Detection: Yes, as a PRIMARY KEY
  - Sensitive Information: No

3. **Description**
  - Data Type: String
  - Default Value: None
  - Range of Values: Alphanumeric
  - Sensitive Information: No
  - Required for Analysis : No

4. **Genre**
  - Data Type: String
  - Range of Values: Categorical
  - Distribution Analysis: TBD
  - Used for Duplicate Detection: No
  - Required: Yes
  - Used in Analysis: Yes, for genre-based success prediction.
  - Sensitive Information: No



5. **Platform**
  - Data Type: String
  - Range of Values: Categorical
  - Distribution Analysis: TBD
  - Unique Values: No
  - Required: Yes
  - Used in Analysis: Yes, for platform-specific analysis.


6. **Reviews**
  - Data Type: Float
  - Types: Best and Worst reviews
  - Default Value: None
  - Range of Values: 0.0 to 10.0
  - Distribution Analysis: Distribution of review scores
  - Required: Yes
  - Used in Analysis: Yes, for assessing critical acclaim.


7. **Development Company**
  - Data Type: String
  - Default Value: None
  - Range of Values: Alphanumeric
  - Distribution Analysis: N/A
  - Unique Values: No
  - Used for Duplicate Detection: No
  - Required: No
  - Used in Analysis: TBD, possible developer-based success analysis.


8. **Release Date**
  - Data Type: Date
  - Default Value: None
  - Range of Values: Date format (YYYY-MM-DD)
  - Distribution Analysis: Timeline of release dates
  - Required: Yes
  - Used in Analysis: TBD, possibly for temporal analysis.


9. **Review Date**
  - Data Type: Date
  - Range of Values: Date format (YYYY-MM-DD)
  - Distribution Analysis: Timeline of review dates
  - Unique Values: No
  - Used for Duplicate Detection: No
  - Required: Yes
  - Used in Analysis: Yes, for understanding the time between release and review.

## BIBLIOGRAPHY:
**Giant Bomb:** https://www.giantbomb.com/api/documentation/
**Moby Games:** https://www.mobygames.com/info/api/
**IGDB:** https://www.igdb.com/api
How did you collect your data?
Via API requests and extraction of JSON files provided by Moby Games
Is the source reputable? 
Yes, these platforms are leaders in providing information and databases for games.

## About Data Cleanliness : 
We limited the extraction of missing values for reviews and companies from the IGDB API requests. As for the rest of our sources, we did not encounter relevant issues that can compromise our analysis.

## Are there duplicates? Do these occur in fields that are important for your project's goals?
Since one of the main things we’re focused on is numerical rates and reviews, we do have reviews of different games. However in this case it is a good thing because we wanted to match this to the average reviews of igdb, our largest data base.


## Attributes to disregard: 
Perhaps data about game descriptions and additional information such as links to cover images (as seen in Moby Games). We are considering removing descriptions as our analysis will focus on other attributes rather than a language model. 

## Are there any data type issues?
We haven’t run into any data type issues yet. Except for the release date in the IGDB data which varies in format. 





