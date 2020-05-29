$(document).ready(function() {

	$('#taskButton').click(function() {
		var serializedData = $('#createTaskForm').serialize();

		$.ajax({
			url: $('#createTaskForm').data('url'),
			data: serializedData,
			type: 'post',
			success: function(response) {
				$('#taskList').append('<div class="card mb-2" id="taskCard">' +
										'<div class="card-body">'
											+ response.task.title +
											'<button type="button" class="close" aria-label="Close">' +
		          								'<span aria-hidden="true">&times;</span>' +
		        							'</button>' +
										'</div>' +
									'</div>'
				)
			}
		});

	});


});
