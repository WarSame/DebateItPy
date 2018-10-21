import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { User } from '../user';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-create-user',
  templateUrl: './create-user.component.html',
  styleUrls: ['./create-user.component.css']
})
export class CreateUserComponent implements OnInit {
  private form: FormGroup;
  private user: User;

  name = new FormControl('', Validators.required);
  email = new FormControl('', Validators.required);

  constructor(
    public service: UserService,
    private fb: FormBuilder
  ) {
    this.form = fb.group({
      'name': this.name,
      'email': this.email
    });
  }

  ngOnInit() {
  }

  onSubmit() {
    this.user = new User(
      this.form.value.name,
      this.form.value.email
      );
    this.service.createUser(this.user).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}
