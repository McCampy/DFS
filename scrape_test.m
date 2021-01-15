%% Scraping Data from line star

%% 
% page1v = urlread('https://www.linestarapp.com/Perfect/Sport/NFL/Site/FanDuel/PID/260');
page = webread('https://www.linestarapp.com/Perfect/Sport/NFL/Site/FanDuel/PID/260');

tree = htmlTree(page);
select = 'tbody';
data = findElement(tree,select)

