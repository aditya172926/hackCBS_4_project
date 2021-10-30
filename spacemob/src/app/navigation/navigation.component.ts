import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss'],
})

export class NavigationComponent implements OnInit {
  userId;

  constructor(private userService: UserService, private router: Router) { }

  ngOnInit() {
    this.userId = {'key': localStorage.getItem('user_id') };
  }

  onLogout() {
    console.log(this.userId);
    this.userService.logoutUser(this.userId).subscribe(
      response => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('user_id');
        this.router.navigate(['/login']);
      },
      error => {
        console.log('Error', error);
      }
    );
  }

}
