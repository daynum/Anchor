
$(document).ready(function(){
    $.post("./top_news/",
        {
            topic: "top_news",
        },
        function(data, status){
            var news_list_html = "<div class=\"container\"><h2>Hacker News: TOP NEWS</h2>"
            for ( var i = 0; i < data.news_list.length; i++) {
                var obj = data.news_list[i];
                news_list_html+="<div class=\"card border-info mb-3 card-body\">"+
                            "<h5 class=\"card-title\"><a href=\""+obj.link+"\" target=\"_blank\" >"+obj.title+"</a></h5>"+
                            "<p class=\"card-text\">"+obj.description+"</p>"+"</div>"
            }
            news_list_html += ("</div>")
            $("#news-content").html(news_list_html);
        }
    );
})