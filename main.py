import redditQuestion #Get the latest question
import backgroundImg #Get new background image
import textToVideo #Convert audio to video

#Get question data
questionData = redditQuestion.get_latest_question()

#Downlaod new wallpaper
backgroundImg.downloadNewWallpaper()

textToVideo.converter(questionData["question"], "th.jpg")