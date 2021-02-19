function sortChoices()
{
    let choice_div = document.getElementsByClassName("choice")[0]

    let choice_wrappers = choice_div.getElementsByClassName("choice-wrapper")
    let choice_wrap_list = []

    for (let i=0;i<choice_wrappers.length;i++)
    {
        choice_wrap = choice_wrappers[i]
        score = choice_wrap.getElementsByClassName("votes-number")[0].getElementsByTagName("p")[0].innerHTML.split(" ")[0]
        score = parseInt(score)
        newobj = {"score":score, "html":choice_wrap}
        choice_wrap_list.push(newobj)
    }

    let reverse = false;

    choice_wrap_list.sort(function(a,b){
        let Ascore = a.score;
        let Bscore = b.score;

        if(Ascore > Bscore) return -1;
        if(Ascore < Bscore) return 1;
        return 0;
    })

    if(reverse)
    {
        choice_wrap_list.reverse();
    }

    choice_div.innerHTML = ""
    choice_wrap_list.forEach((choice)=>{
        document.getElementsByClassName("choice")[0].innerHTML += choice.html.outerHTML

    })
}
