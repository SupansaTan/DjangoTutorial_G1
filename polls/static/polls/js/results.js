let reverseVotes = false; // if reverse will be sort ascending
let reverseLastVoteTime = true; // if reverse will be sort date time descending

function sortVoteScore()
{
    /* get container of all choices */
    let choice_div = document.getElementsByClassName("choice")[0]

    /* get choice wrapper */
    let choice_wrappers = choice_div.getElementsByClassName("choice-wrapper")
    let choice_wrap_list = []

    /* get votes for each choice to add object in list */
    for (let i=0;i<choice_wrappers.length;i++)
    {
        choice_wrap = choice_wrappers[i]
        score = choice_wrap.getElementsByClassName("votes-number")[0].getElementsByTagName("p")[0].innerHTML.split(" ")[0] // get score in tag <p> 
        score = parseInt(score)
        choice = {"score":score, "html":choice_wrap}
        choice_wrap_list.push(choice)
    }

    /* sort descending */
    choice_wrap_list.sort(function(a,b){
        let Ascore = a.score;
        let Bscore = b.score;

        if(Ascore > Bscore) return -1;
        if(Ascore < Bscore) return 1;
        return 0;
    })

    /* sort ascending */
    if(reverseVotes)
    {
        choice_wrap_list.reverse();
    }

    /* change sort format and change the arrow in button */
    if(reverseVotes){
        reverseVotes = false; // next times will be sort descending
        $('#arrow_votes').removeClass('arrow up');
        $('#arrow_votes').addClass('arrow down');
    }
    else{
        reverseVotes = true; // next times will be sort ascending
        $('#arrow_votes').removeClass('arrow down');
        $('#arrow_votes').addClass('arrow up');
    }

    /* clear old choices and replace with all choices were sorted on template */
    choice_div.innerHTML = ""
    choice_wrap_list.forEach((choice)=>{
        document.getElementsByClassName("choice")[0].innerHTML += choice.html.outerHTML
    })
}

function sortLastVoteTime()
{
    /* get container of all choices */
    let choice_div = document.getElementsByClassName("choice")[0]

    /* get choice wrapper */
    let choice_wrappers = choice_div.getElementsByClassName("choice-wrapper")
    let choice_wrap_list = []

    /* get time for each choice to add object in list */
    for (let i=0;i<choice_wrappers.length;i++)
    {
        choice_wrap = choice_wrappers[i]
        time = choice_wrap.getElementsByClassName("lasttime-vote")[0].getElementsByTagName("p")[0].innerHTML.split(" ") // get date-time in tag <p> 
        date = time[4].split("/")
        datetime_new_format = date[2].substring(0,4) + "/" + date[1] + "/" + date[0] + " " + time[5]
        choice = {"time":datetime_new_format, "html":choice_wrap}
        choice_wrap_list.push(choice)
    }

    /* sort ascending */
    choice_wrap_list.sort(function(a,b){
        let AdateTime = new Date(a.time);
        let BdateTime = new Date(b.time);
        return new Date(AdateTime) - new Date(BdateTime);
    })

    /* sort descending */
    if(reverseLastVoteTime)
    {
        choice_wrap_list.reverse();
    }

    /* change sort format and change the arrow in button */
    if(reverseLastVoteTime){
        reverseLastVoteTime = false; // next times will be sort ascending
        $('#arrow_voteTime').removeClass('arrow down');
        $('#arrow_voteTime').addClass('arrow up');
    }
    else{
        reverseLastVoteTime = true; // next times will be sort descending
        $('#arrow_voteTime').removeClass('arrow up');
        $('#arrow_voteTime').addClass('arrow down');
    }

    /* clear old choices and replace with all choices were sorted on template */
    choice_div.innerHTML = ""
    choice_wrap_list.forEach((choice)=>{
        document.getElementsByClassName("choice")[0].innerHTML += choice.html.outerHTML
    })
}