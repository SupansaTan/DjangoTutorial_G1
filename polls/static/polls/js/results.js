let reverse = false; // if reverse will be sort ascending

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
    if(reverse)
    {
        choice_wrap_list.reverse();
    }


    /* change sort format and change the arrow in button */
    if(reverse){
        reverse = false;
        $('#arrow').removeClass('arrowup');
        $('#arrow').addClass('arrowdown');
    }
    else{
        reverse = true;
        $('#arrow').removeClass('arrowdown');
        $('#arrow').addClass('arrowup');
    }

    /* clear old choices and replace with all choices were sorted on template */
    choice_div.innerHTML = ""
    choice_wrap_list.forEach((choice)=>{
        document.getElementsByClassName("choice")[0].innerHTML += choice.html.outerHTML
    })
}
