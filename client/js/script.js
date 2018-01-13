function update(){
	var id=document.getElementById('id').value;
	var name=document.getElementById('name').value;
	var dob=document.getElementById('dob').value;
	var phone=document.getElementById('phone').value;
	var email=document.getElementById('email').value;
	var designation=document.getElementById('designation').value;
	var address=document.getElementById('address').value;
	var hobby=document.getElementById('hobby').value;
	var link='127.0.0.1:5000/update?id=' + id + '&name=' + name + '&dob=' + dob +'&phone=' + phone +'&email=' + email + '&designation=' + designation + '&address=' + address + '&hobby=' + hobby
	call(link);

}




function call(link){

	console.log('hy');

	$.ajax({
      	url: link,
      	type:"get",
      	complete:function(){
      		alert("Updated");
      	},
      	error: function (){ 
      		alert("Request Failed"); 
      	}
	});
}