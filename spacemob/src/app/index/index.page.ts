import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-index',
  templateUrl: './index.page.html',
  styleUrls: ['./index.page.scss'],
  providers: [ UserService ]
})
export class IndexPage implements OnInit {
  userdata;

  constructor(private userService: UserService, private router: Router) {
    this.userdata = {
      author: localStorage.getItem('user_id'),
      origin: '',
      continent: '',
      country: ''
    };
    this.userDataGet();
   }

  ngOnInit() {}

  getUserData() {
    this .userService.getUsers(localStorage.getItem('user_id')).subscribe(
      response => {
        console.log(response);
      },
      error => {
        console.log('error', error);
      }
    );
  }

  userDataGet = () => {
    this.userService.getUpdatedUsers(localStorage.getItem('user_id')).subscribe(
      response => {
        console.log(response[0]);
        this.userdata = response[0];
      },
      error  => {
        console.log(error);

      }
    );
  }

  userDataPut() {
    this.userService.putUpdateUsers(this.userdata).subscribe(
      response => {
        console.log(response);
      },
      error  => {
        console.log(error);
      }
    );
  }

  userDataPost() {
    this.userService.postUpdateUsers(this.userdata).subscribe(
      response => {
        console.log(response);
      },
      error => {
        console.log(error);
      }
    );
  }

}
