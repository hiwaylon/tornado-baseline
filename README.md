# DQS - Diet Quality API

Compute quality of meal portions based on a diet quality score.

## Create a portion score.
Send a HTTP `POST` request to `/api/v1/scores` with a JSON body containing
the following data:

    {
        "foodType": <string - key from configured food types>,
        "numberOfPortions": <integer - number of portions to score>,
        "timeStamp": <date - date the portion was consumed>
    }

On success a `201` code will be sent with a JSON response:

    {
        "score": <integer - score of the meal portion>,
        "dayTotal": <integer - score for the day>,
        "weekTotal": <integer - score for the week>,
        "monthTotal": <integer - score for the month>
    }
