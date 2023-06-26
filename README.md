# Covid-19 Spark project 
![GitHub watchers](https://img.shields.io/github/watchers/d-elicio/COVID-19-Spark-project-?style=social) 
![GitHub forks](https://img.shields.io/github/forks/d-elicio/COVID-19-Spark-project-?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/d-elicio/COVID-19-Spark-project-?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/d-elicio/COVID-19-Spark-project-?style=plastic)

Designing and the implementation of different **Spark** applications written in *Python* language to accomplish different jobs used to analyze a dataset on Covid-19 disease created by  [Our World In Data](https://ourworldindata.org/).

Design and implementation in Spark of: 
-  an application returning the classification of **continents** in order of *decreasing* **total_cases**
- an application returning, for each **location**, the *average* number of **new-tests** per day
- an application returning the *5 days* in which the total number of patients in Intensive care units (ICUs) and hospital was highest (**icu_patients+ hosp_patients**), by *decreasing order* of this total number.

All the Spark applications will be executed with **different size of input values** and with **different configurations** (*local, Standalone cluster and with YARN*) to evaluate the different execution times.

## 🚀 About Me
I'm a computer science Master's Degree student and this is one of my university project. 
See my other projects here on [GitHub](https://github.com/d-elicio)!

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://d-elicio.github.io)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/domenico-elicio/)


# 💻 The project

### Dataset
The dataset is a collection of the COVID-19 data manteined and updated daily by *Our World In Data* and contains data on confirmed cases, deaths, hospitalizations, and other variables of potential interest. 

The dataset available in different formats can be found [here](https://github.com/owid/covid-19-data/tree/master/public/data), while the *data dictionary* useful to understand the meaning of all the dataset's columns is available [here](https://github.com/owid/covid-19-data/blob/master/public/data/owid-covidcodebook.csv).

![Data dictionary](https://github.com/d-elicio/COVID-19-MapReduce-project/assets/96207365/127dad45-8243-40d2-80d4-6f0a0fa64d41)

## Job 1
**Implementation of a Spark application that returns the classification of **continents** in order of decreasing **total_cases**.**

An illustrative graph of the various steps performed to solve the problem is shown:

![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/087f3a03-6ea1-4bcc-8b3d-fdd1513445bc)


After importing the functions we need from the different libraries, the first thing to do to permit a Spark application to run, is to create a **SparkSession** which has an **appName** to identify it. After reading the csv file, all the various filtering and required operations are computed to reach our goal:

![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/8a70222a-2dba-4934-9329-1c1879725037)


### Job 1 results:
The execution of this job has been done in all 3 running configurations (*Local mode, Standalone Cluster and withYARN*). 

*Three different types of input data* have been used. Results changes with respect to the inputs:

#### **Input: MARCH-APRIL data**
![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/4036aeeb-2e88-4e55-b25f-f534464d1207)

#### **Input: MARCH-AUGUST data**
![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/d7937469-99c7-4166-8505-7823ac2493bf)

#### **Input: MARCH-OCTOBER data**
![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/dc476d88-226f-48ae-af6f-ebccb1f08584)






## Job 2
**Implementation of a Spark application that returns for each **location** the average number of **new-tests** per day**


An illustrative graph of the various steps performed to solve the problem is shown:

![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/2d658989-aa63-4676-b6e6-c0fbb53fa118)


After importing the functions we need from the different libraries, the first thing to do to permit a Spark application to run, is to create a **SparkSession** which has an **appName** to identify it. After reading the csv file, all the various filtering and required operations are computed to reach our goal:

![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/7d66dcac-e8bb-443b-ba93-88a071ed265d)




### Job 2 results:
The execution of this job has been done in all 3 running configurations (*Local mode, Standalone Cluster and withYARN*). 

*Three different types of input data* have been used. Results changes with respect to the inputs:

#### **Input: MARCH-APRIL data**
![marapr](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/f153fc51-5222-4c50-a3d1-f2a9148d8852)

#### **Input: MARCH-AUGUST data**
![marago](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/17a82878-221e-497e-a1a9-abcba13e5639)

#### **Input: MARCH-OCTOBER data**
![marott](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/e3bdc6a5-e683-46a2-a734-335739399b65)





## Job 3
**Implementation of a Spark application that returns the classification of the **5 days** in which the total number of patients in Intensive Care Unit (ICUs) and hospital (**icu_patients + hosp_patients**) was highest, by decreasing order of this total number**


An illustrative graph of the various steps performed to solve the problem is shown:

![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/aac1d338-12be-4655-b3de-4f86b4fdc26e)

After importing the functions we need from the different libraries, the first thing to do to permit a Spark application to run, is to create a **SparkSession** which has an **appName** to identify it. After reading the csv file, all the various filtering and required operations are computed to reach our goal:

![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/dccdb037-6717-480f-8949-775d04365243)




### Job 3 results:
The execution of this job has been done in all 3 running configurations (*Local mode, Standalone Cluster and withYARN*). 

*Three different types of input data* have been used. Results changes with respect to the inputs:

#### **Input: MARCH-APRIL data**
![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/aac5bffe-2d40-4e59-83aa-ffbf79d64780)

#### **Input: MARCH-AUGUST data**
![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/0e6c2cd7-337d-490f-8ec4-940b905edff7)

#### **Input: MARCH-OCTOBER data**
![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/8d0892f4-b743-43bb-8f38-f945e90becbd)





## Spark configurations time comparison
For every job some tabular and graphical comparison of job's execution times in *local*, *standalone-cluster and with YARN* configurations have been computed. Obviously all these execution times are taken even considering the *different input sizes* used.

![immagine](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/f90c6bf2-e037-4383-aca4-f5cf87f6f787)

![b](https://github.com/d-elicio/COVID-19-Spark-project-/assets/96207365/f1c1778c-69aa-4b23-b517-46223e3b3f3e)



### Time comparison results discussion
- As we expect, the fastest configuration is the **Local mode** and this because in this configuration Spark runs in a *single VM* and using *multiple threads* to do all the computations, and it is why Local configuration is used particularly for the code *debugging* and *testing*.

- On the other way the **Standalone-Cluster** mode is used to simulate the possible behavior of *distributed computation*, but all the part of the managing of the resources is done by Spark internally  in different VM instances on a single machine. 

- These times really increase when the job is ran using **YARN** because the computational times sum up to the times due to resource managing.


## Support
For any support, error corrections, etc. please email me at domenico.elicio13@gmail.com
