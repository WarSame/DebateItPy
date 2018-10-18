import { Component, OnInit } from '@angular/core';
import { CommunityService } from 'src/app/services/community/community.service';
import { Community } from '../community';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-create-community',
  templateUrl: './create-community.component.html',
  styleUrls: ['./create-community.component.css']
})
export class CreateCommunityComponent implements OnInit {
  private form: FormGroup;
  private community: Community;

  name = new FormControl('', Validators.required);
  description = new FormControl('', Validators.required);

  constructor(
    public service: CommunityService,
    private fb: FormBuilder
  ) {
    this.form = fb.group({
      'name': this.name,
      'description': this.description
    });
  }

  ngOnInit() {
  }

  onSubmit() {
    this.community = new Community(
      this.form.value.name,
      this.form.value.description
      );
    this.service.createCommunity(this.community).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}
