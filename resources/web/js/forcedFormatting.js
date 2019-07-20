var leftCharacterUrl = 'https://rcs-image-bucket.s3.amazonaws.com/Melee/Characters/Renders/Left/'
var rightCharacterUrl = 'https://rcs-image-bucket.s3.amazonaws.com/Melee/Characters/Renders/Right/'

document.getElementById('game_round').innerHTML = "{{game.round}}".toUpperCase();
document.getElementById('p1_tag').innerHTML = "{{players.p1_tag}}".toUpperCase();
document.getElementById('p2_tag').innerHTML = "{{players.p2_tag}}".toUpperCase();

var p1Character = "{{players.p1_character}}".toLowerCase();
var p2Character = "{{players.p2_character}}".toLowerCase();

function capitalizeColor(color){
    return color[0].toUpperCase() + color.substring(1).toLowerCase()
}
var p1Color = capitalizeColor("{{players.p1_color}}");
var p2Color = capitalizeColor("{{players.p2_color}}");

var character1Url = leftCharacterUrl + p1Character + '/' + p1Color + '.png';
var character2Url = rightCharacterUrl + p2Character + '/' + p2Color + '.png';

document.getElementById('p1CharacterImage').src = character1Url;
document.getElementById('p2CharacterImage').src = character2Url;
document.body.style.zoom = "70%"