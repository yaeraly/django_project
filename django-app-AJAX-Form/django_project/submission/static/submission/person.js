$(document).ready(function() {
	
	$('#createButton').click('click', function() {
		var serializedData = $('#createPersonForm').serialize();

		$.ajax({

			url: $('#createPersonForm').data('url'),
			data: serializedData,
			type: 'post',
			success: function(response) {
				$('#personList').append('<div class="card mb-3">' +
											'<div class="card-body" id="personCard">'
												+ response.person.full_name +	
												'<button type="button" class="close" aria-label="Close">' +
	         										'<span aria-hidden="true">&times;</span>' +
	        									'</button>' +
											'</div>' +
										'</div>'
										)
									}

		});

		$('#createPersonForm')[0].reset();

	});


	$('')

}); 